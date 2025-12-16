from typing import Dict, Optional, List, Any
import asyncio, httpx
import mimetypes, json
from upload import Upload
from Provides import Provide

class Ask:
    def __init__(self, *, prompt: str, filepath: Optional[List[str]] = None):
        self.prompt = prompt
        self.headers = Provide().headers
        self.cookies = Provide().cookies
        self.result = Upload(filepaths=filepath)
        self.image_url: List[str] = []
        if filepath:
            upload_result = asyncio.run(self.result.get_url())
            self.image_url = [
                item["data"]["url"]
                for item in upload_result
            ]

        self.json_data: Dict[str, Any] = {
            'stream': True,
            'message': {
                'role': 'user',
                'content': prompt,
                'files': [
                    {
                        'url': url,
                        'mimeType': mimetypes.guess_type(filepath[i])[0] or 'image/jpeg',
                        'name': filepath[i],
                    }
                    for i, url in enumerate(self.image_url)
                ] if filepath else []
            },
            'product': 'ai-chat',
            'prompt': {
                'id': 'ai_chat',
            },
            'tools': [],
        }


    async def get(self):
        """Fetch the stream response and return the combined text."""
        async with httpx.AsyncClient(cookies=self.cookies, headers=self.headers, timeout=httpx.Timeout(10.0)) as client:
            response = await client.post(
                'https://quillbot.com/api/raven/quill-chat/responses',
                json=self.json_data
            )
            try:
                self.response_text = response.text
            except AttributeError:
                self.response_text = (await response.aread()).decode()

            result_text = ""
            for line in self.response_text.splitlines():
                line = line.strip()

                if line.startswith("data: {") and '"chunk":"' in line:
                    start = line.find('"chunk":"') + len('"chunk":"')
                    end = line.find('"', start)
                    result_text += line[start:end]

            return result_text

    async def extract_image_id(self):
        for line in self.response_text.splitlines():
            line = line.strip()
            if '"imageIds":[' in line:
                start = line.find('"imageIds":[') + len('"imageIds":[')
                start = line.find('"', start) + 1
                end = line.find('"', start)
                return line[start:end]
        return ""

    async def final(self):
        response = await self.get()
        response = response.replace("\\\\", "")
        return {
            "request": self.prompt,
            "response": response
        }


    def chat(self):
        data =  asyncio.run(self.final())
        return json.dumps(
            data,
            indent=4,
            ensure_ascii=False,
            sort_keys=True
        )


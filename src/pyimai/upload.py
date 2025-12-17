import httpx, asyncio, json
from typing import Optional, Any, List

class Upload:
    def __init__(self, *, filepaths: Optional[List[str]], expiration: int = 600, key: str = "46503be935b7b03b31d903b3dae8397b"):
        self.__filepaths: Any = filepaths or []
        self.url = "https://api.imgbb.com/1/upload"
        self.params = {
            "key": key,
            "expiration": expiration
        }
        self._data: List[str] = []

    async def get_url(self) -> List[str]:
        async with httpx.AsyncClient(timeout=10.0) as client:
            for path in self.__filepaths:
                with open(path, "rb") as image_file:
                    response = await client.post(
                        url=self.url,
                        params=self.params,
                        files={"image": image_file}
                    )

                    data = response.json()
                    self._data.append(data)

        return self._data

    async def get_info(self):
        url = await self.get_url()
        return json.dumps(url, indent=4, ensure_ascii=False, sort_keys=True)


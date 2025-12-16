from typing import Optional, Any, Dict, List

class Provide:
    def __init__(self):
        self.cookies: Dict[str, str] = {
            'abIDV2': '546',
            'anonID': 'f7ceed385778e221',
            'premium': 'false',
            'acceptedPremiumModesTnc': 'false',
            '_sp_ses.48cd': '*',
            'connect.sid': 's%3AoNTyr66sFMpJww2YC1k9jsS5rG8gfAh_.Sm0N0bBqdEBKfsYVLxJ%2FePg%2B%2FyDjynTPY69eA57QGIk',
            'qdid': '78e86ed47333249550c398b65d45ad12',
            'g_state': '{"i_l":0,"i_ll":1765558934871,"i_b":"UI81TLyXP2qutpHvhEmffFoKt+o/llZjjo/FyztB2KA","i_e":{"enable_itp_optimization":0}}',
            '__cf_bm': '1yTH2_Pa300o9uXq6vlgz1sQHyvNOVxMgwJOS1gJYOg-1765559791-1.0.1.1-NrhDeQrGvIsVtea_ZlWVpzWonZzrDka8rL7Ik1iez6CaLJBlJMNR1kO75rPNw9Q0MqReS4bFN7UC0NpbkwTCtBNnIHycBklSM3wo_KAJmCw',
            'useridtoken': 'eyJhbGciOiJSUzI1NiIsImtpZCI6Ijk1MTg5MTkxMTA3NjA1NDM0NGUxNWUyNTY0MjViYjQyNWVlYjNhNWMiLCJ0eXAiOiJKV1QifQ.eyJuYW1lIjoiRGFyayIsInBpY3R1cmUiOiJodHRwczovL2xoMy5nb29nbGV1c2VyY29udGVudC5jb20vYS9BQ2c4b2NLQTlxZkRRZkRaVU5xNk1iYUJrU2NsTGtLRHJUcnh0Rlh4VjhZU3IyWVhBa0wzU3c9czk2LWMiLCJpc3MiOiJodHRwczovL3NlY3VyZXRva2VuLmdvb2dsZS5jb20vcGFyYXBocmFzZXItNDcyYzEiLCJhdWQiOiJwYXJhcGhyYXNlci00NzJjMSIsImF1dGhfdGltZSI6MTc2NTU1OTgxMywidXNlcl9pZCI6ImtMRTc0aXExWTFVM2hSUVB0YmJhelRnTGVhdDEiLCJzdWIiOiJrTEU3NGlxMVkxVTNoUlFQdGJiYXpUZ0xlYXQxIiwiaWF0IjoxNzY1NTU5ODEzLCJleHAiOjE3NjU1NjM0MTMsImVtYWlsIjoiZGVlcGpzeUBnbWFpbC5jb20iLCJlbWFpbF92ZXJpZmllZCI6dHJ1ZSwiZmlyZWJhc2UiOnsiaWRlbnRpdGllcyI6eyJnb29nbGUuY29tIjpbIjEwMDcxMzY2MzU3ODExMTAzMTMxNCJdLCJlbWFpbCI6WyJkZWVwanN5QGdtYWlsLmNvbSJdfSwic2lnbl9pbl9wcm92aWRlciI6Imdvb2dsZS5jb20ifX0.cIHr55tC27Sq_dXUJTUZIgVMItBQnvbi75rF1O-ma820N-1fcVPWh4lNlZDCP_vsKi9BJvXRYI83C0Se6WEBlAR1YC-aybCSD05u_SlYyDNnlkXmOXDJguvwM84KDOMcBZDik76GfRHv3AefqvLk7JSvrYbhmsNr_0CxwR66P87P3VJCEDsjokaJGiE7aLFs06_CMhAVM_g93Gyf-Bxb57oNomdFRYbCwIIWQppPEDRLSXJnmhHiaCHZOqSsgmIkGtz4mZbpeVyIHaN-CbZmci4s8QTvsY8E-_TpocYHGw4XYHdThI61W54jgNVi990cW7edvQfHwehv5Lwxd65tCQ',
            'authenticated': 'true',
            '_sp_id.48cd': '37c7e1f4-cd04-4797-afdf-d0b8e6ae880f.1760000217.3.1765560556.1765046295.8b1ebd61-21c7-4a61-979a-da5382d96e07.61f3f5c0-2893-4aff-b352-b6e5666f54e9.79af7ac3-a5f4-4b93-863e-29c3c8215d08.1765558727252.58',
        }


        self.headers: Dict[str, str] = {
            'accept': 'text/event-stream',
            'accept-language': 'en-US,en;q=0.7',
            'baggage': 'sentry-environment=prod,sentry-release=v38.25.1,sentry-public_key=5743ef12f4887fc460c7968ebb2de54d,sentry-trace_id=fa0126ba335a40b2a55d9a9edd703bd0,sentry-sampled=false,sentry-sample_rand=0.15919515209713975,sentry-sample_rate=0.01',
            'cache-control': 'max-age=0',
            'content-type': 'application/json',
            'origin': 'https://quillbot.com',
            'platform-type': 'webapp',
            'priority': 'u=1, i',
            'qb-product': '',
            'referer': 'https://quillbot.com/ai-chat/c/541c9fee-7b9e-4c23-bf84-aec530f07259',
            'sec-ch-ua': '"Brave";v="143", "Chromium";v="143", "Not A(Brand";v="24"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'sec-gpc': '1',
            'sentry-trace': 'fa0126ba335a40b2a55d9a9edd703bd0-92ea6b36888ca769-0',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36',
            'useridtoken': 'eyJhbGciOiJSUzI1NiIsImtpZCI6Ijk1MTg5MTkxMTA3NjA1NDM0NGUxNWUyNTY0MjViYjQyNWVlYjNhNWMiLCJ0eXAiOiJKV1QifQ.eyJuYW1lIjoiRGFyayIsInBpY3R1cmUiOiJodHRwczovL2xoMy5nb29nbGV1c2VyY29udGVudC5jb20vYS9BQ2c4b2NLQTlxZkRRZkRaVU5xNk1iYUJrU2NsTGtLRHJUcnh0Rlh4VjhZU3IyWVhBa0wzU3c9czk2LWMiLCJpc3MiOiJodHRwczovL3NlY3VyZXRva2VuLmdvb2dsZS5jb20vcGFyYXBocmFzZXItNDcyYzEiLCJhdWQiOiJwYXJhcGhyYXNlci00NzJjMSIsImF1dGhfdGltZSI6MTc2NTU1OTgxMywidXNlcl9pZCI6ImtMRTc0aXExWTFVM2hSUVB0YmJhelRnTGVhdDEiLCJzdWIiOiJrTEU3NGlxMVkxVTNoUlFQdGJiYXpUZ0xlYXQxIiwiaWF0IjoxNzY1NTU5ODEzLCJleHAiOjE3NjU1NjM0MTMsImVtYWlsIjoiZGVlcGpzeUBnbWFpbC5jb20iLCJlbWFpbF92ZXJpZmllZCI6dHJ1ZSwiZmlyZWJhc2UiOnsiaWRlbnRpdGllcyI6eyJnb29nbGUuY29tIjpbIjEwMDcxMzY2MzU3ODExMTAzMTMxNCJdLCJlbWFpbCI6WyJkZWVwanN5QGdtYWlsLmNvbSJdfSwic2lnbl9pbl9wcm92aWRlciI6Imdvb2dsZS5jb20ifX0.cIHr55tC27Sq_dXUJTUZIgVMItBQnvbi75rF1O-ma820N-1fcVPWh4lNlZDCP_vsKi9BJvXRYI83C0Se6WEBlAR1YC-aybCSD05u_SlYyDNnlkXmOXDJguvwM84KDOMcBZDik76GfRHv3AefqvLk7JSvrYbhmsNr_0CxwR66P87P3VJCEDsjokaJGiE7aLFs06_CMhAVM_g93Gyf-Bxb57oNomdFRYbCwIIWQppPEDRLSXJnmhHiaCHZOqSsgmIkGtz4mZbpeVyIHaN-CbZmci4s8QTvsY8E-_TpocYHGw4XYHdThI61W54jgNVi990cW7edvQfHwehv5Lwxd65tCQ',
            'webapp-version': '38.25.1'
        }

        self.cookie: Dict[str, str] = {
            'abIDV2': '546',
            'anonID': 'f7ceed385778e221',
            'premium': 'false',
            'acceptedPremiumModesTnc': 'false',
            '_sp_ses.48cd': '*',
            'connect.sid': 's%3AoNTyr66sFMpJww2YC1k9jsS5rG8gfAh_.Sm0N0bBqdEBKfsYVLxJ%2FePg%2B%2FyDjynTPY69eA57QGIk',
            'qdid': '78e86ed47333249550c398b65d45ad12',
            'g_state': '{"i_l":0,"i_ll":1765558934871,"i_b":"UI81TLyXP2qutpHvhEmffFoKt+o/llZjjo/FyztB2KA","i_e":{"enable_itp_optimization":0}}',
            '__cf_bm': '1yTH2_Pa300o9uXq6vlgz1sQHyvNOVxMgwJOS1gJYOg-1765559791-1.0.1.1-NrhDeQrGvIsVtea_ZlWVpzWonZzrDka8rL7Ik1iez6CaLJBlJMNR1kO75rPNw9Q0MqReS4bFN7UC0NpbkwTCtBNnIHycBklSM3wo_KAJmCw',
            'useridtoken': 'eyJhbGciOiJSUzI1NiIsImtpZCI6Ijk1MTg5MTkxMTA3NjA1NDM0NGUxNWUyNTY0MjViYjQyNWVlYjNhNWMiLCJ0eXAiOiJKV1QifQ.eyJuYW1lIjoiRGFyayIsInBpY3R1cmUiOiJodHRwczovL2xoMy5nb29nbGV1c2VyY29udGVudC5jb20vYS9BQ2c4b2NLQTlxZkRRZkRaVU5xNk1iYUJrU2NsTGtLRHJUcnh0Rlh4VjhZU3IyWVhBa0wzU3c9czk2LWMiLCJpc3MiOiJodHRwczovL3NlY3VyZXRva2VuLmdvb2dsZS5jb20vcGFyYXBocmFzZXItNDcyYzEiLCJhdWQiOiJwYXJhcGhyYXNlci00NzJjMSIsImF1dGhfdGltZSI6MTc2NTU1OTgxMywidXNlcl9pZCI6ImtMRTc0aXExWTFVM2hSUVB0YmJhelRnTGVhdDEiLCJzdWIiOiJrTEU3NGlxMVkxVTNoUlFQdGJiYXpUZ0xlYXQxIiwiaWF0IjoxNzY1NTU5ODEzLCJleHAiOjE3NjU1NjM0MTMsImVtYWlsIjoiZGVlcGpzeUBnbWFpbC5jb20iLCJlbWFpbF92ZXJpZmllZCI6dHJ1ZSwiZmlyZWJhc2UiOnsiaWRlbnRpdGllcyI6eyJnb29nbGUuY29tIjpbIjEwMDcxMzY2MzU3ODExMTAzMTMxNCJdLCJlbWFpbCI6WyJkZWVwanN5QGdtYWlsLmNvbSJdfSwic2lnbl9pbl9wcm92aWRlciI6Imdvb2dsZS5jb20ifX0.cIHr55tC27Sq_dXUJTUZIgVMItBQnvbi75rF1O-ma820N-1fcVPWh4lNlZDCP_vsKi9BJvXRYI83C0Se6WEBlAR1YC-aybCSD05u_SlYyDNnlkXmOXDJguvwM84KDOMcBZDik76GfRHv3AefqvLk7JSvrYbhmsNr_0CxwR66P87P3VJCEDsjokaJGiE7aLFs06_CMhAVM_g93Gyf-Bxb57oNomdFRYbCwIIWQppPEDRLSXJnmhHiaCHZOqSsgmIkGtz4mZbpeVyIHaN-CbZmci4s8QTvsY8E-_TpocYHGw4XYHdThI61W54jgNVi990cW7edvQfHwehv5Lwxd65tCQ',
            'authenticated': 'true',
            '_sp_id.48cd': '37c7e1f4-cd04-4797-afdf-d0b8e6ae880f.1760000217.3.1765560587.1765046295.8b1ebd61-21c7-4a61-979a-da5382d96e07.61f3f5c0-2893-4aff-b352-b6e5666f54e9.79af7ac3-a5f4-4b93-863e-29c3c8215d08.1765558727252.59',
        }

        self.header: Dict[str, str] = {
            'accept': 'application/json, text/plain, */*',
            'accept-language': 'en-US,en;q=0.7',
            'baggage': 'sentry-environment=prod,sentry-release=v38.25.1,sentry-public_key=5743ef12f4887fc460c7968ebb2de54d,sentry-trace_id=fa0126ba335a40b2a55d9a9edd703bd0,sentry-sampled=false,sentry-sample_rand=0.15919515209713975,sentry-sample_rate=0.01',
            'platform-type': 'webapp',
            'priority': 'u=1, i',
            'referer': 'https://quillbot.com/ai-chat/c/541c9fee-7b9e-4c23-bf84-aec530f07259',
            'sec-ch-ua': '"Brave";v="143", "Chromium";v="143", "Not A(Brand";v="24"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'sec-gpc': '1',
            'sentry-trace': 'fa0126ba335a40b2a55d9a9edd703bd0-8463a79b242ad608-0',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36',
            'useridtoken': 'eyJhbGciOiJSUzI1NiIsImtpZCI6Ijk1MTg5MTkxMTA3NjA1NDM0NGUxNWUyNTY0MjViYjQyNWVlYjNhNWMiLCJ0eXAiOiJKV1QifQ.eyJuYW1lIjoiRGFyayIsInBpY3R1cmUiOiJodHRwczovL2xoMy5nb29nbGV1c2VyY29udGVudC5jb20vYS9BQ2c4b2NLQTlxZkRRZkRaVU5xNk1iYUJrU2NsTGtLRHJUcnh0Rlh4VjhZU3IyWVhBa0wzU3c9czk2LWMiLCJpc3MiOiJodHRwczovL3NlY3VyZXRva2VuLmdvb2dsZS5jb20vcGFyYXBocmFzZXItNDcyYzEiLCJhdWQiOiJwYXJhcGhyYXNlci00NzJjMSIsImF1dGhfdGltZSI6MTc2NTU1OTgxMywidXNlcl9pZCI6ImtMRTc0aXExWTFVM2hSUVB0YmJhelRnTGVhdDEiLCJzdWIiOiJrTEU3NGlxMVkxVTNoUlFQdGJiYXpUZ0xlYXQxIiwiaWF0IjoxNzY1NTU5ODEzLCJleHAiOjE3NjU1NjM0MTMsImVtYWlsIjoiZGVlcGpzeUBnbWFpbC5jb20iLCJlbWFpbF92ZXJpZmllZCI6dHJ1ZSwiZmlyZWJhc2UiOnsiaWRlbnRpdGllcyI6eyJnb29nbGUuY29tIjpbIjEwMDcxMzY2MzU3ODExMTAzMTMxNCJdLCJlbWFpbCI6WyJkZWVwanN5QGdtYWlsLmNvbSJdfSwic2lnbl9pbl9wcm92aWRlciI6Imdvb2dsZS5jb20ifX0.cIHr55tC27Sq_dXUJTUZIgVMItBQnvbi75rF1O-ma820N-1fcVPWh4lNlZDCP_vsKi9BJvXRYI83C0Se6WEBlAR1YC-aybCSD05u_SlYyDNnlkXmOXDJguvwM84KDOMcBZDik76GfRHv3AefqvLk7JSvrYbhmsNr_0CxwR66P87P3VJCEDsjokaJGiE7aLFs06_CMhAVM_g93Gyf-Bxb57oNomdFRYbCwIIWQppPEDRLSXJnmhHiaCHZOqSsgmIkGtz4mZbpeVyIHaN-CbZmci4s8QTvsY8E-_TpocYHGw4XYHdThI61W54jgNVi990cW7edvQfHwehv5Lwxd65tCQ',
            'webapp-version': '38.25.1',
        }


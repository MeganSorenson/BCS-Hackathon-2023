import openai,os,sys
from youtube_transcript_api import YouTubeTranscriptApi
import os

class NotRequests(): 

        @staticmethod
        def getCaptions(url):
                #parse url to get video key 
                videoKey = url.split("/watch?v=")[1]

                # of dictionaries obtained by the get_transcript() function
                srt = YouTubeTranscriptApi.get_transcript("SW14tOda_kI")

                captions = ""
                for dic in srt:
                        captions = captions + " " + dic.get("text","")

                # prints the result
                #print(captions)
                NotRequests.getGPT("summarize this: " + captions)
                return captions



        def getGPT(prompt):
                openai.api_key = os.environ['GPT_API_KEY']
                messages = [
                        {"role": "system", "content": "You are a helpful assistant."},
                ]
                while True:
                        messages.append(
                                {"role": "user", "content": prompt},
                        )
                        chat_completion = openai.ChatCompletion.create(
                                model="gpt-3.5-turbo",
                                messages=messages
                        )
                        answer = chat_completion.choices[0].message.content
                        print(f"ChatGPT: {answer}")
                        messages.append({"role": "assistant", "content": answer})
                        return answer



NotRequests.getGPT("hello")
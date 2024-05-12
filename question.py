import random
from typing import List, Dict
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from pymongo import MongoClient
from fastapi import APIRouter, Depends, Request

router = APIRouter()

from mcq.mcqService import McqService
from wordle.wordleService import WordleService

from fastapi import APIRouter, Depends, Request
from fastapi.responses import JSONResponse
import json

from flashcard.flashService import FlashService
from post.postService import PostService
from htmlGames.htmlservice import HtmlService

mcqService = McqService()
wordleService = WordleService()

flashcardService = FlashService()
postService = PostService()
htmlService = HtmlService()
games = [flashcardService,mcqService,postService]
#games = [mcqService,flashcardService]


# Endpoint to get MCQ questions
@router.get("/get-question")
async def get_question(request: Request):
    gameService = mcqService
    question = gameService.get_random_question()
    return JSONResponse(content=question, status_code=200)


@router.get("/get-question/bulk")
async def get_question(request: Request):
    res = []
    # for i in range (8):
    #     gameService = random.choice(games)
    #     question = gameService.get_random_question()
    #     res.append(question)
    htmls=htmlService.get_random_questionbulk()
    res1=htmls+res
    random.shuffle(res1)
    return JSONResponse(content=res1, status_code=200)

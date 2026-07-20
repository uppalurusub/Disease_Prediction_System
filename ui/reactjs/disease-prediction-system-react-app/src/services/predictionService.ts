import type {PredictionRequest} from "../models/PredictionRequest";
import {predictDisease} from "../api/predictionApi";
export const predictionService={predict:(r:PredictionRequest)=>predictDisease(r)};
import api from "./axios";
import type {PredictionRequest} from "../models/PredictionRequest";
import type {PredictionResponse} from "../models/PredictionResponse";
export const predictDisease=async(req:PredictionRequest):Promise<PredictionResponse>=>{
 const {data}=await api.post<PredictionResponse>("/predict/",req);
 return data;
};
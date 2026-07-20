import {useState} from "react";
import type {PredictionRequest} from "../models/PredictionRequest";
import type {PredictionResponse} from "../models/PredictionResponse";
import {predictionService} from "../services/predictionService";
export const usePrediction=()=>{
 const [loading,setLoading]=useState(false);
 const [result,setResult]=useState<PredictionResponse|null>(null);
 const predict=async(r:PredictionRequest)=>{setLoading(true);try{setResult(await predictionService.predict(r));}finally{setLoading(false);}};
 return {loading,result,predict};
};
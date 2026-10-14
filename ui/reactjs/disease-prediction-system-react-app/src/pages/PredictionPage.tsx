import PredictionForm from "../components/prediction/PredictionForm";
import PredictionResult from "../components/prediction/PredictionResult";
import {usePrediction} from "../hooks/usePrediction";
export default function PredictionPage()
{ 
    const {predict,loading,result}=usePrediction();
    return
    <>
        <PredictionForm onSubmit={predict}/>
        { loading&&<p>Loading...</p> }
        { result&&<PredictionResult result={result}/> }
    </>
}

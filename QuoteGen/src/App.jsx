import { useEffect } from "react"
import jobAnimation from './assets/Animation - 1712111764905.json'
import Lottie from 'lottie-react'
import Home from "./Home"
// import VideoRecorder from "./recording"
import AudioCapture from "./VideoRecorder"

import VideoRecorder from "./VideoRecorder"

function App() {

  useEffect(() => {
    fetch('http://localhost:5000/quotes')
    .then((response) => {
      return response.json()
    })
    .then((data) =>{
      localStorage.setItem('quotes', JSON.stringify(data))
    })
  },[])

  return (
    <>
     <div className='app-body'>
      <Home />
    <Lottie animationData={jobAnimation} size={10}/>
    </div> 
 
    </>
  )
}

export default App

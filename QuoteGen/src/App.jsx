import { useEffect } from "react"
import Home from "./Home"

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
    </div>
    </>
  )
}

export default App

import React, { useState } from 'react'

const Home = () => {
    

    let quotes = localStorage.quotes
    quotes = quotes ? JSON.parse(quotes) || [] : [];
    const [quote, setQuote] = useState({})

    const handleClick = (e) => {
        const direction = e.target.innerText
        const idx = quote.index === undefined ? null : quote.index
        console.log(idx)

        fetch('http://localhost:5000/quotes', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({direction, current_index: idx})
        })
        .then((response) => {
            return response.json()
        })
        .then((data) => {
            console.log(data)
            let res = quotes.find((quote) => quote.index == data)
            
            console.log(res)
            setQuote(res)

        })
    } 

  return (
    <>
    <div className='quote-container'>
        <h1 className='quote-heading'>Select a Quote</h1>
        <hr />
        <p className='quote-text'>
        {quote.quote ? quote.quote : 'Click a button to get a quote'} 
        </p>
        <p className='quote-author'>{quote.author ? quote.author : 'Click for author'}</p>
        <hr />
        <div className='button-container'>
            <button onClick={handleClick}>darker</button>
            <button onClick={handleClick}>brighter</button>
        </div>
    </div>
    </>
  )
}


export default Home
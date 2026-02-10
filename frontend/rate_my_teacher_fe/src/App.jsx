import { useState, useEffect } from 'react'
import './App.css'

async function fetchAndSet (setPosts) {
  try{
    console.log(setPosts)
    const response = await fetch("http://127.0.0.1:5000/teacher/123?id=456")
    console.log(response)

    const text = await response.text()
    console.log(text)

    setPosts(text)
  }
  catch(err) {
    console.log(err)
  } 
}

function App () {
  const [count, setCount] = useState(0)

  const [posts, setPosts] = useState("")
  console.log(setPosts)

  return (
    <>
      <div className="card">        
        <button onClick={function(){setCount(count+1)}}>
          count is {count}
        </button>


        <button onClick={function(){fetchAndSet(setPosts)}}>
          posts is {posts}
        </button>
      </div>

    </>
  )
}

export default App

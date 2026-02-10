import { useState, useEffect } from 'react'
import './App.css'

async function fetchAndSet (setPosts, teacherId) {
  try{
    console.log(setPosts)
    const response = await fetch(
      `http://192.168.0.76:5000/teacher/123?id=${teacherId}`
    )
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

  const [teacherId, setTeacherId] = useState("")

  const [posts, setPosts] = useState("")
  console.log(setPosts)

  return (
    <>
      <div className="card">        
        <button onClick={function(){setCount(count+1)}}>
          count is {count}
        </button>

        <input  type="text" value={teacherId} onChange={function(event) {setTeacherId(event.target.value)}}></input>
        <button onClick={function(){fetchAndSet(setPosts, teacherId)}}>
          Call API
        </button>
        <br/>
        <label>{posts}</label>
      </div>

    </>
  )
}

export default App

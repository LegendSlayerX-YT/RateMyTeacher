import { useState, useEffect } from 'react'
import './App.css'

function fetchAndSet(setPosts) {
  
  
}

function App() {
  const [count, setCount] = useState(0)

  const [posts, setPosts] = useState("")

  useEffect(() => {
    fetch("http://127.0.0.1:5000/teacher/123?id=456")
    .then(      
      (response) => {
        console.log(response)
        return response.text()
      }
    )
    .then(
      (body) => {
        console.log(body)
        setPosts(body)
      }
    )
    .catch(
      (err) => {
        console.log(err)
        setPosts(err)
      }
    )
  }, []);

  return (
    <>
      <div className="card">        
        <button onClick={() => setCount(count+1)}>
          count is {count}
        </button>


        <button>
          posts is {posts}
        </button>
      </div>

    </>
  )
}

export default App

import { useState, useEffect } from 'react'
import { useNavigate} from "react-router-dom";
import './App.css'
import ViewRatingApp from './ViewRatingApp.jsx'

async function fetchAndSet (setPosts, teacherId) {
  try{
    console.log(setPosts)
    const response = await fetch(
      `/backend/teacher/123?id=${teacherId}`
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

function Home () {
  const [count, setCount] = useState(0)

  const [teacherId, setTeacherId] = useState("")

  const [posts, setPosts] = useState("")

  const navigate = useNavigate();

  const navigateToViewRating = (teacher_id) => {
    navigate("/view_rating", {"state": {"teacher_id": teacher_id}})
  };

  return (
      <div className="card">        
        <button onClick={function(){setCount(count+1)}}>
          count is {count}
        </button>

        <input  type="text" value={teacherId} onChange={function(event) {setTeacherId(event.target.value)}}></input>
        <button onClick={function(){fetchAndSet(setPosts, teacherId)}}>
          Call API
        </button>
        <label>{posts}</label>

        <button onClick={function(){ navigateToViewRating(teacherId)} }>View Ratings</button>      
      
      </div>
  )
}

export default Home

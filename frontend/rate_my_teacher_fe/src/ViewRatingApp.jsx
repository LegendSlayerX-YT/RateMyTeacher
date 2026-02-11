import { useState, useEffect } from 'react'
import { useLocation } from 'react-router-dom';

function ViewRatingApp () {
  const [count, setCount] = useState(0)
  const location = useLocation()

  return (
      <div className="card">        
        <button onClick={function(){setCount(count+1)}}>
          View Rating App count is {count}
        </button>
        <label>
            Teacher id is {location.state['teacher_id']}
        </label>

      </div>
  )
}

export default ViewRatingApp

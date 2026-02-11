import { useState, useEffect } from 'react'
import { useNavigate,  BrowserRouter as Router, Routes, Route } from "react-router-dom";
import './App.css'
import ViewRatingApp from './ViewRatingApp.jsx'
import Home from './Home.jsx'


function App () {
  return (     
      <Routes>
        <Route path="/" element={<Home />}/>
        <Route path="/view_rating" element={<ViewRatingApp />} />
      </Routes>
  )
}

export default App


import './index.css'
import {BrowserRouter, Route, Routes} from 'react-router-dom'
import MostLikedWorkout from './pages/MostLikedWorkout'
import Auth from './pages/Auth'
import Registr from './pages/Registr'

function App() {


  return (
    <BrowserRouter>
      <Routes>
        <Route path='/mostlikedworkout' element={<MostLikedWorkout/>}/>
        <Route path='/' element={<MostLikedWorkout/>}/>
        <Route path='/auth' element={<Auth/>}/>
        <Route path='/register' element={<Registr/>}/>
      </Routes>
    </BrowserRouter>
  )
}

export default App

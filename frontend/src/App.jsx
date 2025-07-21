import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'
import Home from './pages/Home';
import Login from './pages/Login';
import Register from './pages/Register';
import Dashboard from './pages/Dashboard';
import MenuManagement from './pages/MenuManagement';
import OrderPlacement from './pages/OrderPlacement';
import Billing from './pages/Billing';
import Feedback from './pages/Feedback';
import DeliveryTracking from './pages/DeliveryTracking';
import UserProfile from './pages/UserProfile';

function App() {
  const [count, setCount] = useState(0)

  return (
    <Router>
      <div>
        <a href="https://vite.dev" target="_blank">
          <img src={viteLogo} className="logo" alt="Vite logo" />
        </a>
        <a href="https://react.dev" target="_blank">
          <img src={reactLogo} className="logo react" alt="React logo" />
        </a>
      </div>
      <h1>Vite + React</h1>
      <div className="card">
        <button onClick={() => setCount((count) => count + 1)}>
          count is {count}
        </button>
        <p>
          Edit <code>src/App.jsx</code> and save to test HMR
        </p>
      </div>
      <p className="read-the-docs">
        Click on the Vite and React logos to learn more
      </p>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/login" element={<Login />} />
        <Route path="/register" element={<Register />} />
        <Route path="/dashboard" element={<Dashboard />} />
        <Route path="/menu-management" element={<MenuManagement />} />
        <Route path="/order-placement" element={<OrderPlacement />} />
        <Route path="/billing" element={<Billing />} />
        <Route path="/feedback" element={<Feedback />} />
        <Route path="/delivery-tracking" element={<DeliveryTracking />} />
        <Route path="/user-profile" element={<UserProfile />} />
      </Routes>
    </Router>
  )
}

export default App

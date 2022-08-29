import { HashRouter, Routes, Route } from 'react-router-dom'
import Parents from './pages/parents/Parents';
import Teachers from './pages/teachers/Teachers';
import Students from './pages/students/Students';
import Login from './pages/login/Login';
import { useState } from 'react';

function App() {
  const [username, setUsername] = useState(null);

  return (
    <HashRouter>
      <Routes>
        <Route path="/" element={<Login username={username} setUsername={setUsername} />} />
        <Route path="/students" element={<Students username={username} />} />
        <Route path="/parents" element={<Parents username={username} />} />
        <Route path="/teachers" element={<Teachers username={username} />} />
      </Routes>
    </HashRouter>
  );
}

export default App;

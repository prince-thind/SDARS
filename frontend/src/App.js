import { HashRouter, Routes, Route } from 'react-router-dom'
import Parents from './pages/parents/Parents';
import Teachers from './pages/teachers/Teachers';
import Students from './pages/students/Students';
import Login from './pages/login/Login';

function App() {
  return (
    <HashRouter>
      <Routes>
        <Route path="/" element={<Login />} />
        <Route path="/students" element={<Students />} />
        <Route path="/parents" element={<Parents />} />
        <Route path="/teachers" element={<Teachers />} />
      </Routes>
    </HashRouter>
  );
}

export default App;

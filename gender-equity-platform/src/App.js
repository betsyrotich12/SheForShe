import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Home from './pages/Home';
import Mentorship from './pages/Mentorship';
import Forum from './pages/Forum';
import Stories from './pages/Stories';

function App() {
  return (
      <Router>
          <div>
              <Routes>
                  <Route path="/" element={<Home />} />
                  <Route path="/mentorship" element={<Mentorship />} />
                  <Route path="/forum" element={<Forum />} />
                  <Route path="/stories" element={<Stories />} />
              </Routes>
          </div>
      </Router>
  );
}

export default App;

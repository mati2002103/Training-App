import React from 'react';
import { BrowserRouter as Router, Route, Routes, Navigate } from 'react-router-dom';
import LoginForm from './LoginForm'; // Importujemy formularz logowania
import UserPage from './UserPage'; // Importujemy stronę dla zalogowanych użytkowników

const App = () => {
  const [isAuthenticated, setIsAuthenticated] = React.useState(false);

  // Funkcja do ustawiania autoryzacji, można rozszerzyć o logikę sesji lub tokenów
  const handleLogin = () => setIsAuthenticated(true);

  return (
    <Router>
      <Routes>
        <Route
          path="/login"
          element={<LoginForm onLogin={handleLogin} />} // Przekazujemy funkcję do logowania
        />
        <Route
          path="/userpage"
          element={isAuthenticated ? <UserPage /> : <Navigate to="/login" />}
        />
        <Route path="/" element={<Navigate to="/login" />} />
      </Routes>
    </Router>
  );
};

export default App;

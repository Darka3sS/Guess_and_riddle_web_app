import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'

function App() {
// 1. Crea uno "stato" per memorizzare il nome utente che l'utente digita
  const [username, setUsername] = useState('');

  // 2. Questa funzione si attiva quando il form viene inviato
  const handleSubmit = async (event) => {
    // previene il ricaricamento della pagina (fondamentale!)
    event.preventDefault(); 
    
    // Stampa il nome utente nella console (per ora)
    console.log('Username da inviare:', username);

    //Chiamata al backend
    try {
      const response = await fetch('http://localhost:5000/start', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ username: username }),
      });

      const data = await response.json();
      console.log('Risposta dal backend:', data);
      
      // Qui potresti reindirizzare l'utente a un'altra pagina
      // o mostrare il "prossimo passo" dell'indovinello

    } catch (error) {
      console.error('Errore durante la chiamata a /start:', error);
    }
  };

  // 4. Questo è l'HTML (JSX) che React mostrerà
  return (
    <div className="d-flex flex-column justify-content-center align-items-center vh-100">
      <h1>Inserisci il tuo nome giocatore</h1>
      
      {/* 5. Questo è il "React Form" */}
      <form onSubmit={handleSubmit}>
        <input 
          type="text" 
          name="username" 
          maxLength="20" 
          required 
          value={username} // Il valore è legato allo "stato"
          onChange={(e) => setUsername(e.target.value)} // Aggiorna lo stato a ogni tasto
        />
        <button type="submit">Inizia</button>
      </form>
    </div>
  );
}

export default App;

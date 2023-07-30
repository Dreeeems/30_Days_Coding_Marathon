import React, { useEffect, useState } from "react";
import axios from "axios";
import Home from "./views/home";

function App() {
  /*const [environment, setEnvironment] = useState({});

  useEffect(() => {
    // Fetch environment variables from the backend API
    axios.get("http://127.0.0.1:5000")
      .then((response) => {
        setEnvironment(response.data);
      })
      .catch((error) => {
        console.error("Error fetching environment variables:", error);
      });
  }, []);*/

  return (
    <div>
     <Home/>
   
    </div>
  );
}

export default App;

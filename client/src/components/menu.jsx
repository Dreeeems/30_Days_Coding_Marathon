import React, { useState, useEffect } from 'react';
import fetchData from '../util/api'
import logo from '../assets/img/Dreeeems_logo.png'
const Menu = (props) => {
    const [data, setData] = useState([]);
    const [searchTerm, setSearchTerm] = useState('');
  
    const MovieDatas = async (searchTerm) => {

        fetchData(searchTerm)
          .then(response => {
            setData(response.data);
         
          })
          .catch(error => {
            console.error('Error fetching data:', error);
          });
      };
    
      useEffect(() => {
        // Call the function to send data to the parent whenever 'data' state changes
        props.sendDataToParent(data);
      }, [data]); // This 'useEffect' will trigger whenever 'data' changes
    
    const handleKeyPress = event => {
      if (event.key === 'Enter') {
        MovieDatas(searchTerm);
      }
    };

  return (
    <nav className="bg-gray-800 p-4">
    <div className="container m-auto flex items-center justify-between">
      <div className="flex items-center">
        <img
          className="h-8 w-8 mr-2 rounded-full"
          src={logo}
          alt="Logo"
        />
     
      </div>

      <div className="flex items-center justify-center flex-grow">
        <input
          type="text"
          className="w-full px-4 py-2 rounded-md bg-gray-700 text-white focus:outline-none focus:ring focus:border-blue-300"
          placeholder="Search..."
          onChange={e => setSearchTerm(e.target.value)}
          onKeyPress={handleKeyPress}
        />
      </div>

      <div className="flex items-center">
        <a
          href="https://github.com/your_github_username"
          target="_blank"
          rel="noopener noreferrer"
        >
          <svg
            xmlns="http://www.w3.org/2000/svg"
            fill="none"
            viewBox="0 0 24 24"
            className="h-8 w-8 text-white"
          >
            <path
              fillRule="evenodd"
              d="M12 0C5.372 0 0 5.372 0 12c0 5.303 3.438 9.8 8.205 11.385.6.112.82-.261.82-.577 0-.285-.01-1.04-.015-2.045-3.338.724-4.042-1.55-4.042-1.55-.546-1.385-1.333-1.756-1.333-1.756-1.09-.744.083-.729.083-.729 1.205.083 1.838 1.236 1.838 1.236 1.07 1.828 2.805 1.3 3.49.994.108-.776.42-1.305.764-1.605-2.67-.305-5.467-1.335-5.467-5.93 0-1.31.465-2.38 1.235-3.225-.124-.304-.535-1.525.118-3.176 0 0 1.01-.322 3.3 1.232a11.493 11.493 0 013.005-.403c1.022.004 2.047.137 3.005.403 2.286-1.554 3.294-1.232 3.294-1.232.656 1.65.244 2.872.12 3.176.77.845 1.23 1.916 1.23 3.225 0 4.61-2.803 5.622-5.476 5.922.43.373.816 1.104.816 2.224 0 1.607-.015 2.897-.015 3.286 0 .314.214.687.825.572C20.567 21.795 24 17.298 24 12c0-6.628-5.372-12-12-12z"
              clipRule="evenodd"
            />
          </svg>
        </a>
      </div>
    </div>
  </nav>
  )
}

export default Menu
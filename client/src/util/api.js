import axios from 'axios';

const fetchData = (terms) => {
    console.log(terms)
  return axios.get(`http://127.0.0.1:5000/movie/${terms}`); // Replace with your API endpoint URL
};

export default fetchData;
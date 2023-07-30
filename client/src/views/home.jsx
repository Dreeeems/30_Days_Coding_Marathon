import React, { useState } from 'react';
import Menu from '../components/menu';

const Home = () => {
  const [dataFromChild, setDataFromChild] = useState(undefined);

  const handleDataFromChild = (data) => {
    setDataFromChild(data.results);
    console.log(data)
  };

  return (
    <div>
      <Menu sendDataToParent={handleDataFromChild} />
      {dataFromChild && dataFromChild.length > 0 ? (
        <div className="p-10 grid grid-cols-1 sm:grid-cols-1 md:grid-cols-3 lg:grid-cols-3 xl:grid-cols-3 gap-5">
          {/* Enclose the map function inside curly braces */}
          {dataFromChild.map((item) => (
            <div key={item.id} className="rounded overflow-hidden shadow-lg">
              <img className="w-full" src={"https://image.tmdb.org/t/p/w500/"+item.backdrop_path} alt={item.title} />
              <div className="px-6 py-4">
                <div className="font-bold text-xl mb-2">{item.original_title}</div>
                <p className="text-gray-700 text-base">
                  {item.overview}
                </p>
              </div>
              <div className="px-6 pt-4 pb-2">
                <span className="inline-block bg-gray-200 rounded-full px-3 py-1 text-sm font-semibold text-gray-700 mr-2 mb-2">Original Language : {item.original_language}</span>
                <span className="inline-block bg-gray-200 rounded-full px-3 py-1 text-sm font-semibold text-gray-700 mr-2 mb-2">Release date : {item.release_date}</span>
                <span className="inline-block bg-gray-200 rounded-full px-3 py-1 text-sm font-semibold text-gray-700 mr-2 mb-2">Type : {item.media_type}</span>
              </div>
            </div>
          ))}
        </div>
      ) : (
        <>
          {dataFromChild === undefined && <p>Loading...</p>}
          {dataFromChild !== undefined && dataFromChild.length === 0 && <p>No data available.</p>}
        </>
      )}
    </div>
  );
};


export default Home;

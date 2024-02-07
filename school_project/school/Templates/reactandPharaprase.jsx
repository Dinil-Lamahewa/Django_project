import React, { useState } from 'react';
import Papa from 'papaparse';

const ImportCSV = () => {
  const [csvData, setCSVData] = useState([]);

  const onCSVChange = (e) => {
    Papa.parse(e.target.files[0], {
      header: true,
      skipEmptyLines: true,
      complete: (results) => {
        setCSVData(results.data);
      },
    });
  };

  return (
    <div>
      <input type="file" onChange={onCSVChange} />
      <table>
        <thead>
          <tr>
            {Object.keys(csvData[0]).map((key) => (
              <th key={key}>{key}</th>
            ))}
          </tr>
        </thead>
        <tbody>
          {csvData.map((row, index) => (
            <tr key={index}>
              {Object.values(row).map((value, index) => (
                <td key={index}>{value}</td>
              ))}
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default ImportCSV;
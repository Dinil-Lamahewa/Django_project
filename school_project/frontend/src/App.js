import React, { useState } from "react";
import Papa from "papaparse";

const App = () => {
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
      {csvData.length > 0 && (
        <table>
          <thead>
            <tr>
              <th>School</th>
              <th>Class</th>
              <th>Assessment Area</th>
              {/* Add more headers as needed */}
            </tr>
          </thead>
          <tbody>
            {csvData.map((row, index) => (
              <tr key={index}>
                <td>{row.school_name}</td>
                <td>{row.class_name}</td>
                <td>{row.assessment_area}</td>
                {/* Add more table cells as needed */}
              </tr>
            ))}
          </tbody>
        </table>
      )}
    </div>
  );
};

export default App;
import React, { useState } from 'react';
import axios from 'axios';

const FileUploader = () => {
    const [file, setFile] = useState(null);
    const [error, setError] = useState('');

    const handleFileChange = (e) => {
        setFile(e.target.files[0]);
        setError('');
    };

    const handleUpload = () => {
        if (!file) {
            setError('Please select a file.');
            return;
        }

        const formData = new FormData();
        formData.append('file', file);

        axios.post('http://localhost:8000/upload-csv/', formData)
            .then(response => {
                console.log(response.data.message);
            })
            .catch(error => {
                setError(`Error uploading file: ${error.response ? error.response.data.message : error.message}`);
            });
    };

    return (
        <div>
            <input type="file" onChange={handleFileChange} />
            <button onClick={handleUpload}>Upload</button>
            {error && <p style={{ color: 'red' }}>{error}</p>}
        </div>
    );
};

export default FileUploader;

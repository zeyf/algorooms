// Imports
const express = require('express');
const mongoose = require('mongoose');
const cors = require('cors');

// Initialization
const app = express();

// Start server
app.listen(3000, () => {
    console.log("server running on 3000");
})
 
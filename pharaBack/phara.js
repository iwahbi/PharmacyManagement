const express = require('express');
const mongoose = require('mongoose');
const bodyParser = require('body-parser');
const cors = require('cors');

const app = express();
const PORT = process.env.PORT || 7000;

app.use(cors());
app.use(bodyParser.json());

// MongoDB connection
mongoose.connect('mongodb://localhost:27017/IhssaneWahbiM', {
  useNewUrlParser: true,
  useUnifiedTopology: true,
});

// Importing API routes
const orderRoutes = require('./routes/order'); 
const drugsRoutes = require('./routes/drugs');
const userRoutes = require('./routes/user');

// Using API routes
app.use('/order', orderRoutes);
app.use('/drugs', drugsRoutes);
app.use('/user', userRoutes);

// Start the server
app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});

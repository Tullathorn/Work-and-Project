const express = require('express');
const app = express();
const fs = require('fs');
const authRoutes = require('./auth'); 
const path = require('path');

app.use(express.json());
app.use(express.static('public'));
app.use('/api', authRoutes); 

app.get('/', (req, res) => {
    res.sendFile(__dirname + '/public/index.html');
});

app.post('/update-seats', (req, res) => {
    const { updatedSeats, reservation } = req.body;

    try {
        fs.writeFileSync('public/data.json', JSON.stringify(updatedSeats, null, 2));

        let reservations = [];
        if (fs.existsSync('reservations.json')) {
            const reservationsData = fs.readFileSync('reservations.json', 'utf8');
            reservations = reservationsData ? JSON.parse(reservationsData) : [];
        }
        
        reservations.push(reservation);
        fs.writeFileSync('reservations.json', JSON.stringify(reservations, null, 2));

        res.json({ message: 'Seats updated & Reservation saved' });
    } catch (error) {
        res.status(500).json({ error: 'Failed to update data' });
    }
});

app.get('/admin', (req, res) => {
    res.sendFile(__dirname + '/admin/admin.html');
});

app.post('/addCruiseType', (req, res) => {
    const { cruiseType, windowSeats, centerSeats, price } = req.body;

    if (!cruiseType || windowSeats == null || centerSeats == null || price == null) {
        return res.status(400).json({ message: 'Missing required fields' });
    }

    const filePath = 'public/data.json';

    try {
        const data = JSON.parse(fs.readFileSync(filePath, 'utf8'));

        if (data[cruiseType]) {
            return res.status(409).json({ message: 'Cruise type already exists' });
        }

        const totalSeats = windowSeats + centerSeats;

        data[cruiseType] = {
            totalSeats,
            window: windowSeats,
            center: centerSeats,
            price: price,
            seatPrice: {
                window: 700,
                center: 0
            }
        };

        fs.writeFileSync(filePath, JSON.stringify(data, null, 2));
        res.json({ message: 'Cruise type added successfully' });

    } catch (err) {
        console.error(err);
        res.status(500).json({ message: 'Failed to add cruise type' });
    }
});
// 

app.get('/getReservations', (req, res) => {
    fs.readFile('reservations.json', 'utf8', (err, data) => {
        if (err) {
            return res.status(500).json({ message: "Error reading reservation data" });
        }

        const reservations = JSON.parse(data);
        res.json(reservations);
    });
});

// 
app.post('/deleteCruiseType', express.json(), (req, res) => {
    const cruiseToDelete = req.body.cruiseType;
    const filePath = path.join(__dirname, 'public', 'data.json');

    fs.readFile(filePath, 'utf8', (err, data) => {
        if (err) {
            console.error("❌ Error reading file:", err);
            return res.status(500).json({ message: 'Error reading data file' });
        }

        try {
            const cruises = JSON.parse(data);
            if (!cruises[cruiseToDelete]) {
                return res.status(404).json({ message: 'Cruise type not found' });
            }

            delete cruises[cruiseToDelete];

            fs.writeFile(filePath, JSON.stringify(cruises, null, 2), err => {
                if (err) {
                    console.error("❌ Error writing file:", err);
                    return res.status(500).json({ message: 'Failed to delete cruise type' });
                }

                res.json({ message: `Deleted cruise type: ${cruiseToDelete}` });
            });
        } catch (e) {
            console.error("❌ JSON parse error:", e.message);
            res.status(500).json({ message: 'Invalid data format' });
        }
    });
});

app.get('/getCruiseTypes', (req, res) => {
    const filePath = path.join(__dirname, 'public', 'data.json');

    fs.readFile(filePath, 'utf8', (err, data) => {
        if (err) {
            console.error("❌ Error reading data.json:", err);
            return res.status(500).json({ message: 'Error reading data file' });
        }

        try {
            const cruisesObj = JSON.parse(data);
            console.log("✅ Cruises loaded:", cruisesObj);

            // แปลง object ให้กลายเป็น array
            const cruisesArray = Object.entries(cruisesObj).map(([cruiseType, value]) => ({
                cruiseType,
                ...value
            }));

            res.json(cruisesArray);
        } catch (e) {
            console.error("❌ JSON parse error:", e.message);
            return res.status(500).json({ message: 'Invalid JSON format in data.json' });
        }
    });
});

app.listen(3000, () => console.log('Server running on http://localhost:3000'));

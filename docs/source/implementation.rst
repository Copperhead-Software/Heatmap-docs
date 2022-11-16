implementation
===================================

The implementation of the API is quite simple:

make one request to this address:
``http://api.coppperheadsoftware.co:5000/heatmap/?UID=<your UID here>&activity=<whatever the activity name is>``


.. code-block:: javascript
    import {useState} from 'react';

    const App = () => {
    const [data, setData] = useState();
    const [isLoading, setIsLoading] = useState(false);
    const [err, setErr] = useState('');

    const handleClick = async () => {
        setIsLoading(true);
        try {
        const response = await fetch('http://api.coppperheadsoftware.co:5000/heatmap/?UID=<your UID here>&activity=<whatever the activity name is>');

        if (!response.ok) {
            throw new Error(`Error! status: ${response.status}`);
        }

        const result = await response.json();

        console.log('result is: ', JSON.stringify(result, null, 4));

        setData(result);
        } catch (err) {
        setErr(err.message);
        } finally {
        setIsLoading(false);
        }
    };

    console.log(data);

    return (
        <div>
        <button onClick={handleClick}>button things</button>
        </div>
    );
    };

    export default App;

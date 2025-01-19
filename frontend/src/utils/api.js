export async function fetchData(path) {
    try {
        const baseURL = 'http://127.0.0.1:8000/api/'
        const url = baseURL.concat(path)
        const response = await fetch(url);
        if (!response.ok) throw new Error(`HTTP error! Status: ${response.status}`);
        return await response.json();
    } catch (error) {
        console.error('Error fetching data:', error);
        throw error;
    }
}
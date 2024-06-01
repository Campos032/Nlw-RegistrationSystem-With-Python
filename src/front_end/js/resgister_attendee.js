document.addEventListener('DOMContentLoaded', () => {
    const eventForm = document.getElementById('event-form');

    eventForm.addEventListener('submit', async (e) => {
        e.preventDefault();
        const eventName = document.getElementById('event-name').value;
        const eventEmail = document.getElementById('event-email').value;

        try {
            const response = await fetch('http://localhost:3000/events/<event_id>/register', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ name: eventName, email: eventEmail }),
            });

            if (!response.ok) {
                const errorData = await response.json();
                throw new Error(errorData.error || 'Erro ao cadastrar evento');
            }

            const event = await response.json();
            console.log('Evento cadastrado:', event);
            alert(`Evento cadastrado: ${event.name}`);
        } catch (error) {
            console.error('Erro:', error);
            alert(`Erro: ${error.message}`);
        }
    });
});

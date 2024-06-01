document.addEventListener('DOMContentLoaded', () => {
    const eventForm = document.getElementById('event-form');

    eventForm.addEventListener('submit', async (e) => {
        e.preventDefault();
        const eventTitle = document.getElementById('event-title').value;
        const eventDetails = document.getElementById('event-detail').value;
        const eventSlug = document.getElementById('event-slug').value;
        const eventMaximumAttendees = document.getElementById('event-maximum-attendees').value;

        try {
            const response = await fetch('http://localhost:3000/events', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ title: eventTitle, details: eventDetails, slug: eventSlug, 
                                       maximum_attendees: eventMaximumAttendees }),
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

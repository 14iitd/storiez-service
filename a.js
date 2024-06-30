document.addEventListener('DOMContentLoaded', function() {
    const canvas = new fabric.Canvas('storyCanvas', { backgroundColor: '#f0f0f0' });
    const addEmojiButton = document.getElementById('addEmoji');
    const addPollButton = document.getElementById('addPoll');

    addEmojiButton.addEventListener('click', addEmoji);
    addPollButton.addEventListener('click', addPoll);

    function addEmoji() {
        const emoji = new fabric.Text('😊', {
            left: 50,
            top: 50,
            fontSize: 50,
            fontFamily: 'Arial'
        });
        canvas.add(emoji);
    }

    function addPoll() {
        const pollGroup = new fabric.Group([
            new fabric.Textbox('Enter your question here', {
                left: 100,
                top: 100,
                fontSize: 16,
                width: 200,
                fontFamily: 'Arial',
                editable: true
            }),
            new fabric.Textbox('Option 1', {
                left: 100,
                top: 150,
                fontSize: 16,
                width: 150,
                fontFamily: 'Arial',
                editable: true
            }),
            new fabric.Textbox('Option 2', {
                left: 100,
                top: 180,
                fontSize: 16,
                width: 150,
                fontFamily: 'Arial',
                editable: true
            })
        ]);

        canvas.add(pollGroup);
    }
});

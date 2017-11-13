React
=====

JavaScript библиотека для создания веб страниц

.. code-block:: sh

    npm install react

.. code-block:: html

    <script src="/js/react.js">
    <script src="/js/react-dom.js">


.. toctree::
    :maxdepth: 2

    react/index
    reactdom/index


.. code-block:: html

    <!DOCTYPE html>
    <html>
        <head></head>
        <body>
            <script type="text/javascript" src="http://fb.me/react-with-addons-0.13.3.js">
            <script type="text/javascript" src="http://fb.me/JSXTransormer-0.12.0.js">
            <script type="text/jsx">
                var PLAYER_ID = 'player';
                var playlist = ["1", "2"];

                var Player = React.createClass({
                    render: function(){
                        return(
                            <video src={this.props.src} id={PLAYER_ID}/>
                        );
                    },

                    componentDidMount: function(){
                        document.getElementById(PLAYER_ID).addEventListener('ended', this.onEnded);
                    },

                    componentWillUnmount: function(){
                        document.getElementById(PLAYER_ID).removeEventListener('ended', this.onEnded);  
                    },

                    onEnded: function(){
                        alert("...");

                        var newCurrent = this.state.current + 1;
                        if (newCurrent >= this.props.playlist.length){
                            newCurrent = 0
                        }
                        this.setState({
                            current: newCurrent
                        });
                    }
                });

                var PlayerContainer = React.createClass({
                    render: function(){
                        var src = this.props.playlist[this.state.current];

                        return <Player src={src} onEnded={this.onEnded} />;
                    },

                    getInitialState: function(){
                        return {
                            current: 0
                        };
                    },

                    onEnded: function(){
                        alert("...");
                    }
                });

                // React.render(<Player src="..." />, document.body);
                // React.render(<PlayerContainer playlist={playlist}/>, document.body);
            </script>
        </body>
    </html>




.. code-block:: js

    var Hello = React.createClass({

        render: function(){
            return (
                <div>
                    Hello 
                    <b>{this.props.name}</b>, 
                    <b>{this.state.count}</b>!
                    <button type="button" onClick="{this.increment}">
                        Increment
                    </button>
                <div>
            );
        }

        getInitialState: function(){
            return {
                count: 5
            }
        },

        componentWillMount: function(){
            // до создания
        },

        componentWillUnmount: function(){
            // до удаления
        },

        componentDidMount(){
            // после создания
        },

        componentDidUnmount(){
            // после удаления
        },

        increment: function(){
            this.setState({count: this.state.count + 1});
        }
    });

    React.render(
        <Hello name="ilnurgi/>,
        document.getElementById("container"));


Application.react.js

var React = require('react');

var Application = React.createClass({});

module.exports = Application;


app.js

var React = require('react');
var Application = require('./components/Application.react.js');

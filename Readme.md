# Architecture
The vacation planner application is a complex application that requires analysis of multiple factors while planning the vacation. The application needs to consider the availability of the user, the weather conditions at the destination, the currency exchange rates, and the language of the destination. The application also needs to book the tickets and make the hotel reservations for the user. So the application needs to interact with multiple tools such as the calendar, the travel booking website, and the hotel booking website. So we assume that the application has access to the following APIs:

- Calendar API: The AI agent uses the calendar API to check the availability of the user and plan the vacation accordingly.
- Travel booking website API: The AI agent uses the travel booking website API to book the tickets for the user.
- Hotel booking website API: The AI agent uses the hotel booking website API to make the hotel reservations for the user.
- Weather API: The AI agent uses the weather API to check the weather conditions at the destination and plan the vacation accordingly.
- Currency exchange API: The AI agent uses the currency exchange API to convert the currency of the user to the currency of the destination.
- Language translation API: The AI agent uses the language translation API to translate the user's language to the language of the destination. and etc.

The entire vacation planning can be done by making the use of AI agents. The AI agents can be used to plan the vacation, book the tickets, and make the hotel reservations. The AI agents can be used to interact with the calendar, the travel booking website, and the hotel booking website. The AI agents can be used to analyze the data and make the decisions. There are two approaches to build the application:

## 1. Using a single AI agent
In this approach, a single AI agent is used to build the application. The AI agent is responsible for all the tasks such as planning the vacation, booking the tickets, and making the hotel reservations.

In this approach the AI agent has access to multiple tools such as the calendar, the travel booking website, and the hotel booking website. The AI agent uses these tools to plan the vacation and make the bookings.

### Tech Stack:
- Python 
- Langchain (for AI agent (preferred)) / LallmaIndex (for AI agent(best for RAG))
- APIs (Calendar, Travel booking website, Hotel booking website, Weather, Currency exchange, Language translation)
- Docker (for containerization)
- Kubernetes (for orchestration)
- Any Database (for storing the data)  

### Pros:
- Very simple to build as we have only one AI agent responsible for all the tasks.
- Easy to add more tools as the AI agent has access to all the tools.

### Cons:
- The Execution time of the AI agent will be high as the calls to the APIs will be sequential and require a lot of time.
- Even though we make the calls to the tools parallel. The single agent needs to analyze the data and make the decisions sequentially.
- It is difficult to scale the application as the single agent will be responsible for all the tasks and there will be more time spent on each user request.

## 2. Using multiple AI agents
In this approach, multiple AI agents are used to build the application. Each AI agent is responsible for a specific task such as planning the vacation, booking the tickets, and making the hotel reservations. The AI agents work together to plan the vacation and make the bookings. The AI agents communicate with each other using a message broker such as RabbitMQ or Kafka.

### Tech Stack:
- Python
- Langchain (for AI agents) / LallmaIndex (for AI agents)
- AutoGen/Lallma-Agents/ Crew AI (for multiple AI agents)
- RabbitMQ/Kafka (for message broker)
- APIs (Calendar, Travel booking website, Hotel booking website, Weather, Currency exchange, Language translation)
- Docker (for containerization)
- Kubernetes (for orchestration)
- Any Database (for storing the data)

### Pros:
- The Execution time of the AI agents will be less as the calls to the APIs will be parallel and require less time.
- The AI agents can work together to plan the vacation and make the bookings.
- It is easy to scale the application as the AI agents can work together to handle more user requests.

### Cons:
- Complex to build as we have multiple AI agents responsible for different tasks.
- Difficult to add more tools as the AI agents need to communicate with each other using a message broker.
- The AI agents need to be synchronized to work together to plan the vacation and make the bookings.
- The AI agents need to be monitored and managed to ensure that they are working correctly.
- The AI agents need to be tested to ensure that they are working correctly.

This is very high-level architecture. The actual architecture will depend on the requirements of the application and the tools that are available. The architecture can be modified to suit the requirements of the application and the tools that are available. 

# Important Point
The above architecture is just a high-level architecture. The actual architecture will depend on the requirements of the application and the tools that are available. The architecture can be modified to suit the requirements of the application and the tools that are available. The above mentioned suggestions are just for reference, the actual architecture may vary. We have to consider lot of factors before finalizing the architecture. 

- The langchain and other libraries are in very early stage of development. So, we have to consider the stability of the libraries before using them in the production and also there is lots of error handling and testing required before using them in the production.
- There are so many LLM models available in the market. We have to choose the best model which suits our requirements and also we have to consider the performance of the model before using it in the production.As the agents built using the model might not work for all the scenarios and also we have to consider the cost as it can be very costly to use the models in the production.
- The multi agent system is very complex to build and maintain. We have to consider the complexity of the system before building it. We have to consider the cost of building and maintaining the system before building it. And many companies are trying to build the multi agent system but very few are successful in building it. So, we have to consider the success rate of the multi agent system before building it.





# How to run the application
Here I having given the code for very simple vacation planner AI agent where it has access to only one tool which recommends the user vacation packages based on the location,budget and duration. But this can be scalable to add more tools and build the complex AI agent.

The application can be run by following the below steps:
```bash
$ git clone
$ cd planner
$ pip install -r requirements.txt
$ chainlit run main.py
```
Before this set you OPENAI_API_KEY in the environment variables or it will ask before running the application in the terminal

![Demo Video](https://drive.google.com/file/d/1ckCylGtwX7dGf1POAj2qKybBntzjSijW/view?usp=drive_link)




from datetime import datetime
import  random

class Agent:
    '''
    is_available:type(boolean)
    available_since:type(int) it tells no.of hours
    roles: It is a list of roles supported by agent(type:list)
    '''

    def __init__(self, name_agent, is_available, available_since, roles):
        self.name_agent = name_agent
        self.is_available = is_available
        self.available_since = available_since
        self.roles = roles


class Issue:
    '''
      issue
    '''

    def __init__(self, issue_id, roles):
        self.issue_id = issue_id
        self.roles = roles


class AgentSelector:
    '''
       the main class which selects agent
       :param:list of agents
       :select mode:When an issue comes in we need to present the issue to 1 or many agents based on an agent selection mode
    '''

    def __init__(self, list_of_agent,select_mode):
        self.list_of_agent = list_of_agent
        self.select_mode=select_mode

    def select_agent(self,issue):
        selected_agents=set()
        if self.select_mode=="all_available":
            for agent in self.list_of_agent:
                #check whether role of issue is matched with agents
                for role in issue.roles:
                    if role in agent.roles and agent.is_available:
                        selected_agents.add(agent.name_agent)

        elif self.select_mode=="least_busy":
            temp=self.list_of_agent[0]
            cur_agent=temp
            cur_max=temp.available_since
            # print(type(cur_max))
            for agent in self.list_of_agent:
                if  cur_max> agent.available_since:
                    cur_max=agent.available_since
                    cur_agent=agent
            selected_agents.add(cur_agent.name_agent)


        else:
            agent_random=random.choice(self.list_of_agent)
            selected_agents.add(agent_random.name_agent)

        return selected_agents




#sample test cases
agent1 = Agent("vikas", False, datetime.strptime('07/11/2020 01:45PM', '%m/%d/%Y %I:%M%p'),
           ['technician', 'english'])

agent2= Agent("vineela", True, datetime.strptime('07/12/2019 01:45PM', '%m/%d/%Y %I:%M%p'),
           ['service', 'french'])

agent3 = Agent("tom", True, datetime.strptime('07/11/2019 04:45PM', '%m/%d/%Y %I:%M%p'),
           ['service', 'english'])

list_of_agents = [agent1, agent2, agent3]
issue1 = Issue(issue_id=1, roles=['service', 'english'])
issue2 = Issue(issue_id=1, roles=['technician', 'english'])
list_of_issues = [issue1, issue2]

# Instantiate agent selector here and give select mode from one of three options
#1.all_available
#2.least_busy
#3.random
agent_selector=AgentSelector(list_of_agents,select_mode='least_busy')

selected_agents=agent_selector.select_agent(issue1)
#output of selected agents here
print("selected_agents:",selected_agents)

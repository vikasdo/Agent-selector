import unittest
from datetime import datetime

from agentselection import AgentSelector, Agent, Issue, list_of_agents, list_of_issues


class Testagentselection(unittest.TestCase):


    def test_all_available(self):
        agent_selector = AgentSelector(list_of_agents, select_mode='all_available')
        ans = [{'vineela', 'tom'}, {'tom'}]
        zipped = zip(list_of_issues, ans)
        for i, answer in zipped:
            self.assertEqual(agent_selector.select_agent(i), answer)
    def test_least_busy(self):
        agent_selector = AgentSelector(list_of_agents, select_mode='least_busy')
        ans = [{'tom'}, {'tom'}]
        zipped = zip(list_of_issues, ans)
        for i, answer in zipped:
            self.assertEqual(agent_selector.select_agent(i), answer)
    def test_random(self):
        agent_selector = AgentSelector(list_of_agents, select_mode='random')
        answer=set()
        for agent in list_of_agents:
            answer.add(agent.name_agent)
        for i in list_of_issues:
            val=agent_selector.select_agent(i)
            k=list(val)[0]
            self.assertEqual( k in answer, True)


if __name__ == '__main__':
    unittest.main()

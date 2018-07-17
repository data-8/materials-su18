test = {
  'name': 'Question 4.2.4',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> hazard_rates(summed_mn_data.where('Condition', 'Diet').row(0)) - .05229 < .0001
          True
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': '',
      'teardown': '',
      'type': 'doctest'
    }
  ]
}

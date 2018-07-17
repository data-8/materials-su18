test = {
  'name': 'Question 1.5',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> largest_rate_diseases.labels == ('Year', 'Deadliest Disease')
          True
          >>> largest_rate_diseases.num_rows == num_years
          True
          >>> all(largest_rate_diseases.column(0) == np.arange(1900, 2016))
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

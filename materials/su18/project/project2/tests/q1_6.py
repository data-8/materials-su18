test = {
  'name': 'Question 1.6',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> len(proportion_table.labels)
          2
          >>> proportion_table.num_rows
          2
          >>> np.round(sum(proportion_table.column(1))) == 1
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

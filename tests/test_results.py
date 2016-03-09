from elex.api import maps
import tests


class TestMassRollupBug(tests.ElectionResultsTestCase):
    """
    Adding up all of the level "township" should equal
    the totals for "county" but that's not true for
    Nantucket county, MA and the townships in fips 25019.
    """
    data_url = 'tests/data/20160301_super_tuesday.json'

    def test_number_of_counties(self):
        """
        According to bug #236, we should be 1 county short.
        """
        mass_results = [
            r for r in self.results if r.raceid == '24547'
        ]
        mass_county_results = [
            r for r in mass_results if r.level == 'county'
        ]
        mass_counties = [
            r for r in mass_county_results if r.last == 'Trump'
        ]
        self.assertEqual(len(mass_counties), len(maps.FIPS_TO_STATE['MA']))
# -*- coding: utf-8 -*-
"""Setup/installation tests for this package."""

from dps.sitecontent.testing import IntegrationTestCase
from plone import api


class TestInstall(IntegrationTestCase):
    """Test installation of dps.sitecontent into Plone."""

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if dps.sitecontent is installed with portal_quickinstaller."""
        self.assertTrue(self.installer.isProductInstalled('dps.sitecontent'))

    def test_uninstall(self):
        """Test if dps.sitecontent is cleanly uninstalled."""
        self.installer.uninstallProducts(['dps.sitecontent'])
        self.assertFalse(self.installer.isProductInstalled('dps.sitecontent'))

    # browserlayer.xml
    def test_browserlayer(self):
        """Test that IDpsSitecontentLayer is registered."""
        from dps.sitecontent.interfaces import IDpsSitecontentLayer
        from plone.browserlayer import utils
        self.failUnless(IDpsSitecontentLayer in utils.registered_layers())

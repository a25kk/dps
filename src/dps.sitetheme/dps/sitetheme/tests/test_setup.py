# -*- coding: utf-8 -*-
"""Setup/installation tests for this package."""

from dps.buildout.testing import IntegrationTestCase
from plone import api


class TestInstall(IntegrationTestCase):
    """Test installation of dps.buildout into Plone."""

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if dps.buildout is installed with portal_quickinstaller."""
        self.assertTrue(self.installer.isProductInstalled('dps.buildout'))

    def test_uninstall(self):
        """Test if dps.buildout is cleanly uninstalled."""
        self.installer.uninstallProducts(['dps.buildout'])
        self.assertFalse(self.installer.isProductInstalled('dps.buildout'))

    # browserlayer.xml
    def test_browserlayer(self):
        """Test that IDpsBuildoutLayer is registered."""
        from dps.buildout.interfaces import IDpsBuildoutLayer
        from plone.browserlayer import utils
        self.failUnless(IDpsBuildoutLayer in utils.registered_layers())

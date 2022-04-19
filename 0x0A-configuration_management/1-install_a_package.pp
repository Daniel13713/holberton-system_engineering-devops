#nstall a package with a version and using source
package { 'flask':
  ensure   => '2.1.0',
  provider => 'pip3',
}

# installing flask package using pip3
package { 'flask':
          ensure   => ['2.1.0', 'installed'],
          provider => 'pip3',
}
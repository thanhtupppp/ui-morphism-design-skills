import 'package:flutter/material.dart';

class MaterialDesignDemo extends StatelessWidget {
  const MaterialDesignDemo({super.key});

  @override
  Widget build(BuildContext context) {
    final theme = Theme.of(context);
    return Card(
      elevation: 1,
      child: Padding(
        padding: const EdgeInsets.all(16),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            Text('Material component', style: theme.textTheme.titleMedium),
            const SizedBox(height: 12),
            const TextField(
              decoration: InputDecoration(
                labelText: 'Email',
                helperText: 'We will use this for notifications.',
              ),
            ),
            const SizedBox(height: 12),
            Row(
              children: [
                OutlinedButton(onPressed: () {}, child: const Text('Cancel')),
                const SizedBox(width: 12),
                FilledButton(onPressed: () {}, child: const Text('Save')),
              ],
            ),
          ],
        ),
      ),
    );
  }
}

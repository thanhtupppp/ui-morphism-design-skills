import 'package:flutter/material.dart';

class FlatDesignCard extends StatelessWidget {
  const FlatDesignCard({super.key});

  @override
  Widget build(BuildContext context) {
    return Card(
      elevation: 0,
      shape: RoundedRectangleBorder(
        borderRadius: BorderRadius.circular(8),
        side: BorderSide(color: Theme.of(context).colorScheme.outline),
      ),
      child: Padding(
        padding: const EdgeInsets.all(16),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            Text('Flat surface', style: Theme.of(context).textTheme.titleMedium),
            const SizedBox(height: 12),
            const TextField(decoration: InputDecoration(labelText: 'Name')),
            const SizedBox(height: 12),
            FilledButton(onPressed: () {}, child: const Text('Continue')),
          ],
        ),
      ),
    );
  }
}

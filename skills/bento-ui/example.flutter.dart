import 'package:flutter/material.dart';

class BentoExample extends StatelessWidget {
  const BentoExample({super.key});

  @override
  Widget build(BuildContext context) {
    return LayoutBuilder(
      builder: (context, constraints) {
        final columns = constraints.maxWidth >= 900 ? 3 : (constraints.maxWidth >= 600 ? 2 : 1);
        return GridView.count(
          crossAxisCount: columns,
          crossAxisSpacing: 16,
          mainAxisSpacing: 16,
          childAspectRatio: 1.5,
          children: const [
            Card(child: Center(child: Text('Hero'))),
            Card(child: Center(child: Text('Supporting'))),
            Card(child: Center(child: Text('Utility'))),
          ],
        );
      },
    );
  }
}
